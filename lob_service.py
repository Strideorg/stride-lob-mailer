import os
import lob

lob.api_key = os.environ.get("LOB_API_KEY")

def send_letter(first_name, last_name, address_line1, city, state, zip_code, message_body):

    letter = lob.Letter.create(
        description="Stride CRM Letter",

        to={
            "name": f"{first_name} {last_name}",
            "address_line1": address_line1,
            "address_city": city,
            "address_state": state,
            "address_zip": zip_code
        },

        from_address="adr_496f7a55d581fe8d",

        file=f"""
        <html>
            <body>
                <h1>Hello {first_name}</h1>
                <p>{message_body}</p>
            </body>
        </html>
        """,

        merge_variables={
            "name": first_name
        },

        color=False,
        double_sided=False,
        use_type="marketing"
    )

    return {
        "id": letter.id,
        "url": letter.url
    }
