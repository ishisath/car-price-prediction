{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9486c945-5ac0-4c46-8fa9-fb864a869443",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "==================================================\n",
      "   Used Car Price Prediction System\n",
      "==================================================\n",
      "\n",
      "Enter the car details:\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import joblib, numpy as np, pandas as pd\n",
    "\n",
    "best_model   = joblib.load('best_model.pkl')\n",
    "scaler       = joblib.load('scaler.pkl')\n",
    "top_features = joblib.load('top_features.pkl')\n",
    "all_columns  = joblib.load('all_columns.pkl')\n",
    "\n",
    "print()\n",
    "print(\"=\" * 50)\n",
    "print(\"   Used Car Price Prediction System\")\n",
    "print(\"=\" * 50)\n",
    "print(\"\\nEnter the car details:\\n\")\n",
    "\n",
    "year         = int(input(\"  Year of manufacture (e.g. 2017): \"))\n",
    "km_driven    = int(input(\"  Kilometres driven (e.g. 45000): \"))\n",
    "fuel         = input(\"  Fuel type — Petrol / Diesel / CNG / LPG: \").strip().capitalize()\n",
    "seller_type  = input(\"  Seller type — Individual / Dealer / Trustmark Dealer: \").strip().title()\n",
    "transmission = input(\"  Transmission — Manual / Automatic: \").strip().capitalize()\n",
    "owner        = input(\"  Owner — First Owner / Second Owner / Third Owner: \").strip().title()\n",
    "mileage      = float(input(\"  Mileage (km/ltr) e.g. 17.5: \"))\n",
    "engine       = float(input(\"  Engine CC (e.g. 1200): \"))\n",
    "max_power    = float(input(\"  Max power (bhp) e.g. 82.0: \"))\n",
    "seats        = float(input(\"  Number of seats (e.g. 5): \"))\n",
    "brand        = input(\"  Car brand (e.g. Maruti / Honda): \").strip().capitalize()\n",
    "\n",
    "# Build row matching training schema\n",
    "row = {col: 0 for col in all_columns}\n",
    "\n",
    "if 'year'                   in row: row['year']                   = year\n",
    "if 'km_driven'              in row: row['km_driven']              = km_driven\n",
    "if 'mileage(km/ltr/kg)'    in row: row['mileage(km/ltr/kg)']    = mileage\n",
    "if 'engine'                 in row: row['engine']                 = engine\n",
    "if 'max_power'              in row: row['max_power']              = max_power\n",
    "if 'seats'                  in row: row['seats']                  = seats\n",
    "\n",
    "for col in [f'fuel_{fuel}',\n",
    "            f'seller_type_{seller_type}',\n",
    "            f'transmission_{transmission}',\n",
    "            f'owner_{owner}',\n",
    "            f'brand_{brand}']:\n",
    "    if col in row:\n",
    "        row[col] = 1\n",
    "\n",
    "df_input     = pd.DataFrame([row])\n",
    "df_input_sel = df_input[top_features]\n",
    "df_scaled    = scaler.transform(df_input_sel)\n",
    "price        = best_model.predict(df_scaled)[0]\n",
    "\n",
    "print()\n",
    "print(\"=\" * 50)\n",
    "print(\"  PREDICTION RESULT\")\n",
    "print(\"=\" * 50)\n",
    "print(f\"  {brand} ({year}) | {fuel} | {transmission}\")\n",
    "print(f\"  KM Driven: {km_driven:,} | Power: {max_power} bhp\")\n",
    "print()\n",
    "print(f\"  ★ Predicted Selling Price: ₹ {price:,.0f}\")\n",
    "print(\"=\" * 50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23ad5fd9-fb07-4d70-95bc-14862c310839",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
