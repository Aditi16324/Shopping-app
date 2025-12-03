import streamlit as st

st.set_page_config(page_title="Trendy Dresses", layout="wide")

st.title("👗 Trendy Dresses for Women")

# Sample product data
products = [
    {
        "name": "Floral Summer Dress",
        "price": 39.99,
        "description": "Light, airy and perfect for warm days.",
        "image": "https://via.placeholder.com/250x300?text=Floral+Dress"
    },
    {
        "name": "Elegant Evening Gown",
        "price": 89.99,
        "description": "A graceful gown for special occasions.",
        "image": "https://via.placeholder.com/250x300?text=Evening+Gown"
    },
    {
        "name": "Casual Denim Dress",
        "price": 49.99,
        "description": "Comfortable and stylish for everyday wear.",
        "image": "https://via.placeholder.com/250x300?text=Denim+Dress"
    }
]

# Initialize cart
if "cart" not in st.session_state:
    st.session_state.cart = []

st.subheader("✨ Browse Our Collection")

cols = st.columns(3)

for i, product in enumerate(products):
    with cols[i]:
        st.image(product["image"], use_column_width=True)
        st.markdown(f"### {product['name']}")
        st.write(product["description"])
        st.markdown(f"**Price:** ${product['price']}")
        
        if st.button(f"Add to Cart 🛒", key=i):
            st.session_state.cart.append(product['name'])
            st.success(f"Added {product['name']} to cart!")

st.sidebar.header("🛒 Your Cart")
if st.session_state.cart:
    for item in st.session_state.cart:
        st.sidebar.write(f"• {item}")
else:
    st.sidebar.write("Your cart is empty.")
