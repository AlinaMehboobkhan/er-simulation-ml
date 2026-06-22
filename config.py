CONFIG = {
    "SIM_HOURS": 24,
    "NUM_DOCTORS": 5,
    "NUM_BEDS": 20,
    "AVG_ARRIVAL_RATE": 8,
    "RANDOM_SEED": 42,
}
SEVERITY_LABELS = {1: "Critical", 2: "Urgent", 3: "Minor"}
SEVERITY_PROBS  = [0.15, 0.35, 0.50]
TRIAGE_TIMES    = {1: 2, 2: 5, 3: 10}
TREATMENT_MEANS = {1: 45, 2: 35, 3: 25}
