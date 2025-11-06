from database import get_db,    Sessionlocal
from models import DbUser
from hash import Hash

# Database session open karo
db = Sessionlocal()

# Saare users nikaalo
users = db.query(DbUser).all()

for user in users:
    # Check karo ki password already bcrypt hash hai ya nahi
    # bcrypt password hamesha "$2b$" se start hota hai
    if not user.password.startswith("$2b$"):
        print(f"[FIXING] User: {user.username} ka password hash kiya ja raha hai...")
        user.password = Hash.bcrypt(user.password)

# Changes commit karo
db.commit()
db.close()

print("✅ Saare plain-text passwords ab bcrypt hash me convert ho gaye!")
