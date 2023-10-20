#script permettant de créer la database vierge

db_name="bdd_imc_calculator.db"

sqlite3 "$db_name" <<EOF

.databases
.exit
EOF

