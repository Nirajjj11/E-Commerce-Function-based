"""
ML Module 2: Regional Demand Classification using K-Means
Clusters states into High / Medium / Low demand zones
"""

from sklearn.cluster import KMeans
import numpy as np

def get_regional_clusters(seller=None):
    try:
        from store.models import OrderItem
        import numpy as np
        from sklearn.cluster import KMeans

        items = OrderItem.objects.filter(product__seller=seller) if seller else OrderItem.objects.all()

        if not items.exists():
            return []

        state_sales = {}

        for item in items:
            state = getattr(item.order.user, "state", None) or "Unknown"
            state_sales[state] = state_sales.get(state, 0) + item.quantity

        if len(state_sales) < 3:
            return [
                {"state": k, "sales": v, "label": "Insufficient Data"}
                for k, v in state_sales.items()
            ]

        states = list(state_sales.keys())
        sales = np.array(list(state_sales.values())).reshape(-1, 1)

        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(sales)

        results = []
        for i, state in enumerate(states):
            cluster = clusters[i]

            if cluster == np.argmax(kmeans.cluster_centers_):
                label = "High Demand"
            elif cluster == np.argmin(kmeans.cluster_centers_):
                label = "Low Demand"
            else:
                label = "Medium Demand"

            results.append({
                "state": state,
                "sales": int(sales[i][0]),
                "cluster": int(cluster),
                "label": label
            })

        return sorted(results, key=lambda x: x["sales"], reverse=True)

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return []