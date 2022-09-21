class Jorgen:
    def __init__(self):
        self.stilling = "Fullstack-utvikler"
        self.arbeidsgiver = "Tietoevry Banking"
        self.stack = {"database": "MariaDB",
                      "backend": "PHP",
                      "frontend": "AngularJS"}
        self.arbeidserfaring = [
            "maskiningeniør",
            "lydmann",
            "lærer",
            "tekstforfatter",
            "prosjektleder",
            "it manager",
            "salgssjef/økonomisjef",
        ]

    def current_work(self):
        print(self.stilling)
        print(self.arbeidsgiver)
        print(f"Stack: {self.stack}")

    def work_experience(self):
        for jobb in self.arbeidserfaring:
            print(jobb)
