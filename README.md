> [!WARNING]
> ### **LEGAL DISCLAIMER**
> **Navo.ai is a legal logic engine built for educational and informational purposes only.** > I am a JD student, not a licensed attorney. Navo.ai is **not** a law firm and does not provide legal advice. Use of this tool does not create an attorney-client relationship. Always consult a licensed attorney for official legal representation.

> [!IMPORTANT]
> **Beta Release Notice:** This project is currently in a "Limited Open Beta" for 7 days. On [Insert Date], this repository will move to a private license to begin professional refinements.

© 2026 Navo.ai | All Rights Reserved.

# Navo - Legal Situation Explainer

**Help people understand confusing legal situations in plain English — without giving legal advice.**

## The Problem

People facing legal issues often don't know what's happening to them. They can't afford attorneys, don't know where to start, and end up confused or making uninformed decisions.

Traditional solutions:
- ❌ **Hire a lawyer** → Too expensive for most people ($300-500/hour)
- ❌ **Use AI for legal advice** → Massive liability risk, hallucinations, unauthorized practice of law
- ❌ **Read legal websites** → Written in legalese, hard to understand, often irrelevant

## The Solution

**Navo explains legal situations in plain English WITHOUT giving legal advice.**

### What Navo Does:
✅ Explains what a situation might involve  
✅ Shows common factors people in similar situations notice  
✅ Lists questions people often ask attorneys  
✅ Provides emotional clarity and grounding  
✅ Uses plain English, not legal jargon  

### What Navo Does NOT Do:
❌ Give legal advice  
❌ Tell people what to do  
❌ Make predictions about case outcomes  
❌ Evaluate case strength  
❌ Suggest legal strategy  

**This keeps Navo legally safe while still being genuinely helpful.**

## How It Works

1. **User describes their situation** in plain English
2. **Navo explains** what's generally involved in similar situations
3. **User understands** enough to know what questions to ask a real attorney

**Example:**

*User Input:*
> "I got pulled over and the officer searched my car without permission. He found something that wasn't mine. What's happening?"

*Navo Response:*
> **Plain-English Overview:** This situation might involve Fourth Amendment search and seizure issues, which deal with when police can search your property and what happens if they find something.
>
> **Common Factors:** People in similar situations often notice whether the officer had "probable cause" (a good reason to believe evidence was present), whether consent was actually given, and who the item belonged to.
>
> **What People Consider:** Many people think about whether the search was legal, whether evidence can be excluded if it wasn't, and how ownership of items is proven.
>
> **Questions for Counsel:** People often ask attorneys: "Was the search legal without my consent?", "Can the evidence be suppressed?", "What does 'constructive possession' mean?", and "What are my options?"
>
> *This isn't legal advice — just a general explanation to help you understand what you're dealing with until you seek counsel.*

## Installation

```bash
# Clone the repository
git clone https://github.com/BeestoSeesto/navo.git
cd navo

# Install dependencies
pip install -r requirements.txt

# Set up your API key
cp .env.example .env
# Edit .env and add your Anthropic API key
```

## Get API Key

Sign up at: https://console.anthropic.com/  
Free tier: $5 credit (enough for ~100-200 explanations)

## Usage

### Option 1: Web Interface (Recommended)

```bash
streamlit run app.py
```

Opens in your browser at `http://localhost:8501`

### Option 2: Command Line

```bash
python navo.py
```

Type your situation, get an explanation.

## Why This Approach Works

### Legally Safe
- No legal advice = No unauthorized practice of law
- Clear disclaimers throughout
- Educational purpose only
- Encourages consulting real attorneys

### Actually Helpful
- Reduces confusion and anxiety
- Helps people ask better questions when they DO see attorneys
- Makes legal concepts accessible
- Provides emotional grounding

### Serves Underserved Populations
- Free to use (just API costs)
- No legal jargon
- Accessible from anywhere
- Bilingual potential (English/Spanish)

## Technical Stack

- **Python 3.8+**
- **Claude Sonnet 4.5** (via Anthropic API)
- **Streamlit** (web interface)
- **Structured system prompts** (no training required)

## Roadmap

**Phase 1 (Current):** Basic situation explanations  
**Phase 2:** Spanish language support  
**Phase 3:** Document upload (explain eviction notices, court papers, etc.)  
**Phase 4:** Jurisdiction-specific information  
**Phase 5:** Integration with legal aid resources

## Example Use Cases

- **Self-represented litigants** understanding court procedures
- **Tenants** reading eviction notices
- **People arrested** trying to understand charges
- **Employees** facing workplace disputes
- **Anyone** confused by legal documents or situations

## What Makes This Different

**vs. ChatGPT/Claude directly:**
- Structured to avoid legal advice
- Consistent output format
- Built-in disclaimers
- Designed for legal education specifically

**vs. LegalZoom/Rocket Lawyer:**
- Free (just API costs)
- No forms to fill out
- Just explanations, not services
- Clearer about limitations

**vs. Legal aid websites:**
- Interactive, not static
- Personalized to user's situation
- Plain English, not legalese
- Immediate responses

## Limitations

⚠️ **This tool does NOT:**
- Provide legal advice
- Replace attorneys
- Guarantee accuracy for specific cases
- Create attorney-client privilege
- Work for complex legal analysis

**This tool DOES:**
- Help people understand situations generally
- Reduce confusion and anxiety
- Prepare people for attorney consultations
- Make legal concepts more accessible

## Author

**Built by Sisto** - First-year law student at Taft Law School with background in cybersecurity.

This project combines:
- **Legal education** (understanding what people need explained)
- **Technical skills** (building accessible tools)
- **Crisis counseling experience** (providing clarity without causing panic)

**Contact:**  
Email: sistozavala777@gmail.com  
LinkedIn: https://www.linkedin.com/in/sisto-zavala/  
GitHub: https://github.com/BeestoSeesto

## License

MIT License - See LICENSE file

## Contributing

Contributions welcome! Especially:
- Spanish translations
- Improved prompts
- Additional disclaimer options
- UI/UX improvements
- Mobile responsiveness

## Legal Disclaimer

**This software is for educational purposes only.** It does not provide legal advice, create an attorney-client relationship, or replace consultation with a licensed attorney. Always consult a qualified attorney for advice on your specific legal situation.

---

**Note:** If you're facing a legal issue, please seek help from:
- Legal Aid organizations in your area
- State Bar associations (often have referral services)
- Law school clinics
- Pro bono programs

**This tool is meant to help you understand enough to know WHAT to ask when you DO speak with counsel.**
