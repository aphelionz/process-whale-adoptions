import os
import shopify

api_key = os.getenv("SHOPIFY_API_KEY")
password = os.getenv("SHOPIFY_PASSWORD")
shop_url = "https://ocean-alliance-shop.myshopify.com/admin/api/{}".format('2019-04')

shopify.ShopifyResource.set_site(shop_url)
shopify.ShopifyResource.set_user(api_key)
shopify.ShopifyResource.set_password(password)

def _get_all_resources(resource, **kwargs):
    resources = []

    resource_count = resource.count(**kwargs)
    if resource_count > 0:
        result = resource.find(**kwargs)
        while result.has_next_page():
            print(result[0])
            resources.extend(result)
            if result.has_next_page():
                result = result.next_page()
                continue

            break

    return resources

def get_all_shopify_orders():
  return _get_all_resources(shopify.Order)
  