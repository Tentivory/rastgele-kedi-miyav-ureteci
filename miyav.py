#!/usr/bin/env python3
# Rastgele Kedi Miyav Üreteci
# Bu kod kedilerin dilini çözmeye çalışmaz. Sadece miyavlar.

import random

miyavlar = [
    "Miyav.",
    "Miiyaaav!",
    "Miyav miyav.",
    "Prrrr... miyav.",
    "Miyav?",
    "MIAU!",
    "Miyav miyav miyav (açım).",
    "Miyav. (dünyayı yargılıyorum)",
    "Miyav miyav. (özür dilerim kedi değilim)",
    "*sessiz miyav*"
]

def gizli():
    # Saklı: her miyav bir protestodur. Ama kediler öyle düşünmez.
    # Base64: a2VkaWxlciB5önetmez (kediler yönetmez)
    pass

print("Kedi Miyav Makinesi açıldı.")
print(random.choice(miyavlar))
print("Tekrar çalıştır, yeni miyav gelsin.")
