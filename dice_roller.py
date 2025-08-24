{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4b4c4b4a-d5c1-41b4-b688-97491bfcf001",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dice Roller Game\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Press Enter to roll the dice \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You rolled a 1!\n",
      "Next person chance\n"
     ]
    }
   ],
   "source": [
    "import random \n",
    "\n",
    "def roll_dice():\n",
    "    return random.randint(1,6)\n",
    "\n",
    "print(\"Dice Roller Game\")\n",
    "while True:\n",
    "    input(\"Press Enter to roll the dice\")\n",
    "    result = roll_dice()\n",
    "    print(f\"You rolled a {result}!\")\n",
    "\n",
    "    if result == 6:\n",
    "        print(\"You rolled a 6! Roll again\")\n",
    "        continue\n",
    "    else:\n",
    "        print(\"Next person chance\")\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71603449-cf6a-44fc-9a5a-e39cc3a8c6da",
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
