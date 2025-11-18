# MINIMAL ACT TURNOVER SYSTEM
## Simple State Handoff Between Acts

---

## 🔄 CONCEPT

**Problem:** Loading all 3 acts = 32,600 tokens  
**Solution:** Load 1 act at a time, pass minimal state forward  
**Result:** ~9,600 tokens per session (70% reduction)

---

## 📤 ACT 1 → ACT 2 HANDOFF

**Add to end of Act 1:**

```markdown
---

## ✅ ACT 1 COMPLETE

**Copy this state block for Act 2:**

```yaml
[ACT1_EXPORT]
party_level: 5
companions:
  velryn: [loyalty_score or "not_recruited"]
  gralk: [loyalty_score or "not_recruited"]
reputation:
  surface: [score]
  duergar: [score]
  gnomes: [score]
  myconids: [score]
  undead: [score]
key_decisions:
  duergar_market: [trade/liberation/stealth/combat]
  korag: [negotiated/fought/bypassed]
```

**Players:** Level up to 5, take short rest  
**DM:** Start Act 2 with above state
```

**Total addition: ~150 words**

---

## 📤 ACT 2 → ACT 3 HANDOFF

**Add to end of Act 2:**

```markdown
---

## ✅ ACT 2 COMPLETE

**Copy this state block for Act 3:**

```yaml
[ACT2_EXPORT]
party_level: 7
companions:
  velryn: [loyalty_score or "captured/dead"]
  gralk: [loyalty_score or "absent"]
  korag: [recruited: yes/no]
reputation:
  surface: [score]
  duergar: [score]
  gnomes: [score]
  myconids: [score]
  undead: [score]
  drow: [score]
  mindflayers: [score]
blessings:
  durins: [yes/no]
  mourners: [yes/no]
key_status:
  velryn_alive: [yes/no]
  drow_stance: [truce/hostile/dead]
```

**Check Ending 4 Requirements:**
- ✓ Velryn loyalty ≥10 OR PC volunteers
- ✓ Durin's blessing = yes
- ✓ Myconids ≥3
- ✓ Mindflayers ≥3

**Players:** Level up to 7, take long rest  
**DM:** Start Act 3 with above state
```

**Total addition: ~200 words**

---

## 📥 ACT IMPORT SECTIONS

**Add to start of Act 2:**

```markdown
---

## 📥 IMPORT STATE FROM ACT 1

**Paste your Act 1 export here:**

```yaml
[ACT1_EXPORT]
# Paste exported state here
```

*System will initialize Act 2 with these values.*

**Quick validation:**
- ✓ Party level = 5
- ✓ Companion loyalty scores noted
- ✓ Reputation scores recorded

**Begin Act 2**
```

**Total addition: ~80 words**

---

**Add to start of Act 3:**

```markdown
---

## 📥 IMPORT STATE FROM ACT 2

**Paste your Act 2 export here:**

```yaml
[ACT2_EXPORT]
# Paste exported state here
```

*System will calculate available endings from these values.*

**Ending 4 available if:**
- Velryn ≥10 (or PC volunteers) + Durin's blessing + Myconids ≥3 + Mindflayers ≥3

**Begin Act 3 - THE FINALE**
```

**Total addition: ~100 words**

---

## 📊 TOTAL IMPACT

```yaml
additions_per_act:
  act_1_end: ~150 words (~200 tokens)
  act_2_start: ~80 words (~100 tokens)
  act_2_end: ~200 words (~260 tokens)
  act_3_start: ~100 words (~130 tokens)
  
total_added: ~530 words (~690 tokens total)

per_act_increase:
  act_1: +200 tokens (2% increase)
  act_2: +360 tokens (3.7% increase)
  act_3: +130 tokens (1.5% increase)

token_savings_from_modular_loading:
  before: 32,600 (load all 3 acts)
  after: ~9,600 (load 1 act at a time)
  savings: 23,000 tokens (70%)

net_benefit: MASSIVE
```

---

## ✅ IMPLEMENTATION

### **What to Add:**

1. **Act 1 (end):** Export block + level up instruction
2. **Act 2 (start):** Import prompt
3. **Act 2 (end):** Export block + ending check
4. **Act 3 (start):** Import prompt + ending calculator

### **What NOT to Add:**

- ❌ Long templates
- ❌ Detailed instructions
- ❌ Character export forms
- ❌ DM checklists
- ❌ Player handouts

### **Philosophy:**

> **Copy a YAML block. Paste it. Done.**

---

**END OF MINIMAL TURNOVER SYSTEM**

```
[SIMPLE]
[CLEAN]
[EFFECTIVE]
[~700_TOKENS_TOTAL]
```
