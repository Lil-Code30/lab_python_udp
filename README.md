# Laboratoire – Introduction aux sockets

## Objectif du laboratoire

L'objectif de ce laboratoire est de vous familiariser avec la programmation de réseaux en Python à travers l'utilisation de sockets UDP et de vous initier au concept de validation de l’intégrité des données avec la bibliothèque hashlib pour le hachage.

### Matériel nécessaire

- Python 3.x installé sur votre ordinateur
- Accès à un terminal ou à un IDE

## Loko Ismael

### Questions

1. Expliquez en 2–3 phrases pourquoi len(s) peut être différent de len(b).

   **Réponse:**

   > len(s) compte le nombre de caractères utf-8 dans le texte, alors que len(b) compte le nombre de bytes reels dans le fichier. Le format utf-8 utilise un nombre de variable d'octet variable pour chaque caractère. Pour un caractère du plan ASCII, un seul octet sera utilisé. Par contre, les caractères non-ASCII occuperont plus d'un octet d'où la différence entre le nombre de caractères de la chaine et sa taille en octets dans le cas général.

2. Pourquoi les sockets envoient-elles des bytes plutôt que des str ?

   **Réponse:**

   > parce que la communications réseau sont basées sur le transfert des bytes (chaîne d’octets)

3. Quelle différence entre digest() et hexdigest() ?

   **Réponse:**

   > digest() renvoie le hash sous forme binaires (octets) tandis que hexdigest() renvoie le hash sous forme textuelles (hexadécimal).

4. À quoi sert un nonce dans un échange réseau ?

   **Réponse:**

   > Garantit que chaque échange est unique.
