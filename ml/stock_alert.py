from django.utils import timezone
from datetime import timedelta
from ml.stock_predictor import predict_stock


def check_and_generate_stock_alerts(seller):
    try:
        from store.models import Product, OrderItem, StockAlert
        from django.db.models import Sum

        products = Product.objects.filter(
            seller=seller,
            is_active=True
        )

        ago30 = timezone.now() - timedelta(days=30)

        for product in products:
            sold = OrderItem.objects.filter(
                product=product,
                order__order_date__gte=ago30
            ).aggregate(
                total=Sum("quantity")
            )["total"] or 0

            predicted_demand = predict_stock(
                sold,
                product.stock_quantity
            )

            if product.stock_quantity < predicted_demand:
                StockAlert.objects.update_or_create(
                    product=product,
                    is_resolved=False,
                    defaults={
                        "predicted_demand": predicted_demand,
                        "current_stock": product.stock_quantity
                    }
                )

    except Exception as e:
        print("Stock Alert Error:", e)