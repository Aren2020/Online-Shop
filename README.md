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

6. **Login in Stripe**:
   Set your stripe keys then login
   ```sh
   docker-compose exec stripe-cli stripe login
   ```
7. **Restart the container**
   ```sh
   docker-compose down
   docker-compose up
   ```

9. **Access the Application**:
   Open your web browser and navigate to `http://localhost:80`.
