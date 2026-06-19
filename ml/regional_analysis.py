def get_regional_clusters(seller=None):
    try:
        from store.models import OrderItem
        import numpy as np
        from sklearn.cluster import KMeans

        items = OrderItem.objects.filter(product__seller=seller) if seller else OrderItem.objects.all()

        if not items.exists():
            return []

        # ── STEP 1: Aggregate state sales ───────────────
        state_sales = {}

        for item in items:
            state = getattr(item.order.user, "state", None) or "Unknown"
            state_sales[state] = state_sales.get(state, 0) + item.quantity

        states = list(state_sales.keys())
        values = np.array(list(state_sales.values())).reshape(-1, 1)

        # ── STEP 2: fallback for small data ─────────────
        if len(states) < 3:
            return [
                {
                    "state": s,
                    "sales": int(v),
                    "label": "Low Data"
                }
                for s, v in zip(states, values.flatten())
            ]

        # ── STEP 3: safe clustering ─────────────────────
        n_clusters = min(3, len(states))

        if n_clusters < 2:
            return [
                {
                    "state": s,
                    "sales": int(v),
                    "label": "Single Region"
                }
                for s, v in zip(states, values.flatten())
            ]

        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(values)

        centers = kmeans.cluster_centers_.flatten()

        # sort cluster centers
        sorted_idx = np.argsort(centers)

        low_cluster = sorted_idx[0]
        high_cluster = sorted_idx[-1]

        results = []

        for i, state in enumerate(states):
            cluster = clusters[i]

            if cluster == high_cluster:
                label = "High Demand"
            elif cluster == low_cluster:
                label = "Low Demand"
            else:
                label = "Medium Demand"

            results.append({
                "state": state,
                "sales": int(values[i][0]),
                "cluster": int(cluster),
                "label": label
            })

        return sorted(results, key=lambda x: x["sales"], reverse=True)

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return []