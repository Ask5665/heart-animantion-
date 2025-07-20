# 💖 Heart Animation in Python

This project creates a beautiful animated heart using Python and Matplotlib. It’s a fun way to show love through code — maybe even impress your special someone 💌.

---

## 🎞️ Heart GIF

<p align="center">
  <img src="heart.gif" alt="Heart Animation" width="300">
</p>

---

## 🧠 How It Works

The animation is based on this **mathematical equation**:

\[
y = |x|^{2/3} + 0.9*sin(kx)*sqrt{3 - x^2}
\]

### 💡 What This Means:

- `|x|^{2/3}` makes the **basic heart shape**, curved at the top and pointy at the bottom.
- `√(3 - x²)` keeps the shape within a certain range to form a neat outline.
- `sin(kx)` adds a **pulsing or beating effect** to the heart.
- `k` changes over time in the animation, making it "breathe."

So this equation draws a heart and makes it beat, just like a real one — all using math 💓.

---

## 🛠️ What You Need

Make sure you have Python and these libraries:

```bash
pip install numpy matplotlib pillow
