import os
import lob

# ==============================
# STEP 1 — LOAD API KEY
# ==============================

api_key = os.getenv("LOB_API_KEY")

if not api_key:
    raise ValueError("LOB_API_KEY not found. Please export it in the terminal.")

lob.api_key = api_key
print("✅ Lob API key loaded")

# ==============================
# STEP 2 — CREATE TEST LETTER
# ==============================

letter = lob.Letter.create(
    description="Stride CRM Test Letter",
    use_type="marketing",   
    to={
        "name": "John Doe",
        "address_line1": "210 King St",
        "address_city": "San Francisco",
        "address_state": "CA",
        "address_zip": "94107",
        "address_country": "US"
    },
    from_address={
        "name": "Stride CRM",
        "address_line1": "123 Business Rd",
        "address_city": "Austin",
        "address_state": "TX",
        "address_zip": "73301",
        "address_country": "US"
    },
    file="""
    <html>
      <body>
        <h1>Hello from Stride CRM</h1>
        <p>This is a test letter sent using Lob.</p>
      </body>
    </html>
    """,
    color=False,
    double_sided=False
)

# ==============================
# STEP 3 — OUTPUT
# ==============================

print("✅ Letter created successfully")
print("Letter ID:", letter["id"])
print("Preview URL:", letter["url"])