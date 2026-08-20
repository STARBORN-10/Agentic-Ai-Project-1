from google import genai


# ============================================================
# 1. GEMINI API KEY
# ============================================================

API_KEY = "Your API Key"

client = genai.Client(api_key=API_KEY)


# ============================================================
# 2. ART TOOL
# ============================================================

def art_tool(prompt: str, style: str = "realistic") -> dict:
    """
    Use this tool when the user wants to create an image,
    artwork, illustration, advertisement, product image,
    poster, logo, or any other visual content.
    """

    print("\n")
    print("=" * 60)
    print("🎨 GEMINI IS CALLING: ART TOOL")
    print("=" * 60)

    print(f"📝 Prompt : {prompt}")
    print(f"🎨 Style  : {style}")

    # --------------------------------------------------------
    # Put your actual image generation API here later.
    # --------------------------------------------------------

    print("⚙️  Art tool is executing...")

    result = {
        "status": "success",
        "tool": "art_tool",
        "prompt": prompt,
        "style": style,
        "message": "Image generation request processed."
    }

    print("✅ ART TOOL FINISHED")
    print("=" * 60)

    return result


# ============================================================
# 3. PRODUCT TOOL
# ============================================================

def product_tool(
    product_name: str,
    max_price: float = 0,
    category: str = ""
) -> dict:
    """
    Use this tool when the user wants to find, search,
    compare, or recommend products.
    """

    print("\n")
    print("=" * 60)
    print("🛒 GEMINI IS CALLING: PRODUCT TOOL")
    print("=" * 60)

    print(f"📦 Product      : {product_name}")
    print(f"💰 Maximum Price: ₹{max_price}")
    print(f"📂 Category     : {category}")

    # --------------------------------------------------------
    # Put your actual product search API here later.
    # --------------------------------------------------------

    print("⚙️  Product tool is executing...")

    # Dummy results for testing
    results = [
        {
            "name": "Example Gaming Laptop",
            "price": 64999,
            "currency": "INR"
        },
        {
            "name": "Example Performance Laptop",
            "price": 69999,
            "currency": "INR"
        }
    ]

    print(f"🔎 Found {len(results)} products")
    print("✅ PRODUCT TOOL FINISHED")
    print("=" * 60)

    return {
        "status": "success",
        "tool": "product_tool",
        "product": product_name,
        "max_price": max_price,
        "category": category,
        "results": results
    }


# ============================================================
# 4. CALCULATOR TOOL
# ============================================================

def calculator_tool(expression: str) -> dict:
    """
    Use this tool when the user wants to perform
    mathematical calculations.
    """

    print("\n")
    print("=" * 60)
    print("🧮 GEMINI IS CALLING: CALCULATOR TOOL")
    print("=" * 60)

    print(f"📐 Expression: {expression}")

    try:

        # Basic calculator for testing
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        print(f"✅ Result: {result}")
        print("✅ CALCULATOR TOOL FINISHED")
        print("=" * 60)

        return {
            "status": "success",
            "tool": "calculator_tool",
            "expression": expression,
            "result": result
        }

    except Exception as e:

        print("❌ Calculator error:", e)
        print("=" * 60)

        return {
            "status": "error",
            "tool": "calculator_tool",
            "error": str(e)
        }


# ============================================================
# 5. REGISTER ALL TOOLS
# ============================================================

tools = [
    art_tool,
    product_tool,
    calculator_tool
]


# ============================================================
# 6. GEMINI MODEL
# ============================================================

MODEL = "gemini-3.6-flash"


# ============================================================
# 7. CHAT FUNCTION
# ============================================================

def chat():

    print("\n")
    print("=" * 70)
    print("🤖 GEMINI 2.5 TOOL-CALLING AGENT")
    print("=" * 70)

    print("\nAvailable tools:")
    print("🎨 art_tool")
    print("🛒 product_tool")
    print("🧮 calculator_tool")

    print("\nGemini will automatically decide which tool to use.")
    print("Type 'exit' to stop.")
    print("=" * 70)

    while True:

        # ----------------------------------------------------
        # Get user input
        # ----------------------------------------------------

        user_input = input("\n👤 You: ")

        if user_input.lower().strip() == "exit":

            print("\n👋 Agent stopped.")
            break

        if not user_input.strip():

            print("⚠️ Please enter something.")

            continue

        print("\n🤖 Gemini is thinking...")

        try:

            # ------------------------------------------------
            # Send request to Gemini
            # ------------------------------------------------

            response = client.models.generate_content(
                model=MODEL,
                contents=user_input,
                config={
                    "tools": tools
                }
            )

            # ------------------------------------------------
            # Print Gemini response
            # ------------------------------------------------

            print("\n🤖 Gemini:")
            print(response.text)

        except Exception as e:

            print("\n")
            print("=" * 60)
            print("❌ ERROR")
            print("=" * 60)

            print(e)

            print("=" * 60)


# ============================================================
# 8. START PROGRAM
# ============================================================

if __name__ == "__main__":

    chat()

    