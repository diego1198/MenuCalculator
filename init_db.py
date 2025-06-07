from app import app, db, MenuItem

def init_db():
    with app.app_context():
        # Clear existing data
        MenuItem.query.delete()
        
        # Sample menu items
        menu_items = [
            # Comidas
            MenuItem(name="Yahuarlocro", price=3.50, category="Comidas"),
            MenuItem(name="Caldo de gallina", price=3.50, category="Comidas"),
            MenuItem(name="Pollo asado", price=3.50, category="Comidas"),
            
            
            # Bebidas
            MenuItem(name="Cervez 2x5", price=5, category="Bebidas"),
            MenuItem(name="Gaseosa", price=0.75, category="Bebidas"),
            MenuItem(name="Come y bebe", price=1, category="Bebidas"),
            MenuItem(name="Helado", price=1, category="Bebidas"),
        ]
        
        # Add items to database
        for item in menu_items:
            db.session.add(item)
        
        db.session.commit()
        print("Base de datos inicializada con éxito!")

if __name__ == "__main__":
    init_db() 