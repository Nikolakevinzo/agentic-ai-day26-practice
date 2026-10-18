machine_name = "Tube Mill"
base_price = 1200000
gst_rate = 18

gst_amount = base_price * gst_rate / 100
total_price = base_price + gst_amount

print(f"Machine: {machine_name}")
print(f"Base Price: ₹{base_price:,.2f}")
print(f"GST ({gst_rate}%): {gst_amount:,.2f}")
print(f"Total Price: ₹{total_price:,.2f}")
