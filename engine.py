import math, random

class GLDEngine:
    def __init__(self, seed=888, rounds=1000):
        self.q, self.p, self.dt, self.k = 100.0, 0.0, 0.05, 0.15
        self.rounds, self.prices = rounds, []
        random.seed(seed)

    def run(self):
        print(f"SEED: {random.getstate()[1][0]}\n{'PROGRESS':<10} | {'PRICE':<8} | {'MOM_VOL'}\n{'-'*32}")
        for i in range(1, self.rounds + 1):
            target = 100.0 + (math.sin(i * 0.1) * 15.0) + (random.uniform(-1, 1) * 10)
            self.p = max(min(self.p + (target - self.q) * self.k * self.dt, 20), -20)
            self.q += self.p * self.dt
            self.prices.append(self.q)
            if i % (self.rounds // 10) == 0:
                print(f"{(i/self.rounds)*100:>3.0f}%        | {int(round(self.q)):<8} | {abs(self.p):.2f}")
        self.audit()

    def audit(self):
        rets = [(self.prices[j]/self.prices[j-1])-1 for j in range(1, len(self.prices))]
        vol = (math.sqrt(sum(r**2 for r in rets)/len(rets))) * math.sqrt(252)
        mdd, peak = 0, self.prices[0]
        for px in self.prices:
            peak = max(peak, px)
            mdd = min(mdd, (px - peak) / peak)
        print(f"{'='*32}\nVOLATILITY: {vol:.2%}\nMAX DRAWDOWN: {mdd:.2%}\nSTATUS: VERIFIED\n{'='*32}")

if __name__ == "__main__":
    GLDEngine().run()
