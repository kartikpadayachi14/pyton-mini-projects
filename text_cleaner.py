{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4c1cc540-3ba6-4993-a29b-b7f4d161e0d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter text:  i m excited about python\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Words: 5\n",
      "Unique: {'excited', 'm', 'about', 'python', 'i'}\n",
      "Grequency: {'i': 1}\n",
      "Grequency: {'i': 1, 'm': 1}\n",
      "Grequency: {'i': 1, 'm': 1, 'excited': 1}\n",
      "Grequency: {'i': 1, 'm': 1, 'excited': 1, 'about': 1}\n",
      "Grequency: {'i': 1, 'm': 1, 'excited': 1, 'about': 1, 'python': 1}\n"
     ]
    }
   ],
   "source": [
    "import string\n",
    "\n",
    "sentence = input(\"Enter text: \")\n",
    "sentence = sentence.lower()\n",
    "\n",
    "for ch in string.punctuation:\n",
    "    sentence = sentence.replace(ch, \"\")\n",
    "\n",
    "words = sentence.split()\n",
    "print(\"Words:\", len(words))\n",
    "print(\"Unique:\", set(words))\n",
    "\n",
    "freq = {}\n",
    "for w in words:\n",
    "    freq[w] = freq.get(w,0)+1\n",
    "    print(\"Grequency:\",freq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3946efa0-2f9c-4f41-b788-ea17ba9d7930",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
