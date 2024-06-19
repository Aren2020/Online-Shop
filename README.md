### Ecommerce Application

#Create a fully-featured on-line shop

-Build the models of the product catalog
-Create a shopping cart using Django sessions
-Create custom context processors
-Manage customer orders
-Send asynchronous notifications using Celery and RabbitMQ
-Monitory Celery using Flower
-Integrate Stripe to process payments
-Implement a webhook to receive payment notifications from Stripe
-Build custom views in the Django administration site
-Create admin actions and generate CSV files
-Create a coupon system to apply disconts to orders
-Integrate discounts with Stripe payments
-Build a product recommendation engine using Redis
-Add internationalization to the shop
-Generate and manage translation files
-Use Rosetta to manage translations
-Translate URL patterns and build a language selector
-Translate models using django-parler
-Localize forms using django-localflavor


### Steps

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Aren2020/MyShopWeb.git
   cd EducaWeb
   ```

2. **Build the Docker Image**:
   ```sh
   docker-compose build
   ```

3. **Run the Docker Containers**:
   ```sh
   docker-compose up
   ```

4. **Apply Migrations**:
   ```sh
   docker-compose exec web python manage.py migrate
   ```

5. **Create a Superuser**:
   ```sh
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the Application**:
   Open your web browser and navigate to `http://localhost:80`.
