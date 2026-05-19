import numpy as np
 
 
class Ransac:
 
    def __init__(self, iterace=200, prah=5000, seed=42):
        self.iterace = iterace
        self.prah = prah
        # Používáme NumPy random generator pro reprodukovatelnost
        self.rng = np.random.default_rng(seed)
 
    def fituj(self, x, y):
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)
        n = len(x)
 
        nejlepsi_k, nejlepsi_b = 0.0, np.median(y)
        nejlepsi_inliers = np.zeros(n, dtype=bool)
 
        for _ in range(self.iterace):
            # Vyber 2 náhodných bodů a nafitujou se na přímku
            
            idx = self.rng.choice(n, size=2, replace=False)
            A = np.stack([x[idx], np.ones(2)], axis=1)
            k, b = np.linalg.lstsq(A, y[idx], rcond=None)[0]
 
            # Kolmá vzdálenost všech bodů od té přímky
            dist = np.abs(k * x - y + b) / np.sqrt(k**2 + 1)
            inliers = dist < self.prah
 
            # Zapamatuj nejlepší
            if inliers.sum() > nejlepsi_inliers.sum():
                nejlepsi_inliers = inliers
                nejlepsi_k = k
                nejlepsi_b = b
 
        # Přefituj přímku přes všechny inliers najednou
        if nejlepsi_inliers.sum() >= 2:

            #np .stack nám vytvoří 2D pole, kde první sloupec jsou x hodnoty inliers a druhý sloupec jsou jedničky (pro b).
            A = np.stack([x[nejlepsi_inliers], np.ones(nejlepsi_inliers.sum())], axis=1)

            # lstsq funguje tak že vrací pole koeficientů pro všechny sloupce, takže [0] nám vezme jen ten první sloupec, což jsou naše k a b.
            nejlepsi_k, nejlepsi_b = np.linalg.lstsq(A, y[nejlepsi_inliers], rcond=None)[0]
 
        x_unique = np.sort(np.unique(x))
 
        return {
            "k": nejlepsi_k,
            "b": nejlepsi_b,
            "inliers": nejlepsi_inliers,
            "x_unique": x_unique,
            "predikce": nejlepsi_k * x_unique + nejlepsi_b,
        }
 
    def predikuj(self, fit, mesic):
        return fit["k"] * mesic + fit["b"]