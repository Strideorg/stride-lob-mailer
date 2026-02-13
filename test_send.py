from lob_service import send_letter

response = send_letter(
    recipient_name="Jane Investor",
    address_line1="210 King St",
    city="San Francisco",
    state="CA",
    zip_code="94107",
    message_body="We are interested in purchasing your land. Call us today."
)

if response:
    print("✅ Letter sent")
else:
    print("❌ Letter failed")
