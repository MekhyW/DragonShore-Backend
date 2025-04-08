# Dragonshore Backend

Backend for the website of Dragonshore Studios.

All updates, insertions and deletions (CUD) are done via the administration dashboard, at least for now.


## Products Endpoints

### List all products

```http
GET /api/products/
```
Returns a paginated list of active products with basic information and thumbnail URLs

- Supports filtering: <i>?type=premade</i>
- Supports search: <i>?search=keyword</i>
- Supports ordering: <i>?ordering=price_usd or ?ordering=-created_at</i>


### Get product details

```http
GET /api/products/{id}/
```
Returns detailed product information including all associated media


### List products by type

```http
GET /api/products/premade/
GET /api/products/customizable/
GET /api/products/commission_based/
```



## Product Media Endpoints

### List all product media

```http
GET /api/product-media/
```
Returns all product media entries
- Supports filtering: <i>?product=1&file_type=image&thumbnail=true</i>


### Get media details

```http
GET /api/product-media/{id}/
```
Returns detailed information about a specific media item



## Commissions Endpoints

### List all commissions

```http
GET /api/commissions/
```
Returns a paginated list of commissions with basic information
- Supports filtering: <i>?status=queued&product=1</i>
- Supports ordering: <i>?ordering=-created_at</i>


### Get commission details

```http
GET /api/commissions/{id}/
```
Returns detailed commission information including status updates and related product


### List commissions by status

```http
GET /api/commissions/status/{status}/
```
Valid status values: <i>'queued', 'in_progress', 'completed', 'cancelled'</i>



## Commission Status Endpoints

### List all status updates

```http
GET /api/commission-status/
```
Returns all commission status updates
- Supports filtering: <i>?commission=1</i>
- Default ordering is newest first


### Get status update details

```http
GET /api/commission-status/{id}/
```
Returns detailed information about a specific status update
