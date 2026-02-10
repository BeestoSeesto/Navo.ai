# Navo - Quick Start Guide

## Get Running in 3 Minutes

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Get API Key

1. Go to: https://console.anthropic.com/
2. Sign up (free $5 credit)
3. Create API key
4. Copy it

### Step 3: Set Up Environment

```bash
cp .env.example .env
```

Edit `.env` and paste your API key:
```
ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### Step 4: Run Navo

**Web Interface (Recommended):**
```bash
streamlit run app.py
```

Opens at: http://localhost:8501

**Command Line:**
```bash
python navo.py
```

## Try It

**Example situation to test:**

> "I got an eviction notice that says I have 3 days to pay rent or move out. I already paid my rent last week but my landlord says he didn't receive it. What's happening?"

**Navo will explain:**
- What this situation typically involves
- Common factors in similar situations
- What people usually think about
- Questions to ask an attorney

## What You'll See

The explanation follows this format:
1. **Plain-English Overview** - What this might relate to
2. **Common Factors** - What people in similar situations notice
3. **Considerations** - What people think about
4. **Questions for Counsel** - What to ask an attorney
5. **Disclaimer** - This isn't legal advice

## Cost

Each explanation costs approximately $0.02-0.05 in API credits.

With $5 free credit, you can run ~100-200 explanations.

## Common Issues

**Error: "No API key found"**
- Make sure `.env` file exists
- Check that `ANTHROPIC_API_KEY` is set correctly
- No quotes needed around the key

**Streamlit not found**
- Run: `pip install streamlit`

**Port already in use**
- Run: `streamlit run app.py --server.port 8502`

## Next Steps

1. **Try different situations** - See how Navo explains various legal issues
2. **Test the boundaries** - Ask for legal advice and see how Navo refuses appropriately
3. **Customize the prompt** - Edit `navo.py` to adjust the system prompt
4. **Add features** - Spanish support, document upload, etc.

## Deploy Online (Optional)

**Streamlit Community Cloud (Free):**
1. Push to GitHub
2. Go to: https://streamlit.io/cloud
3. Connect your repo
4. Add `ANTHROPIC_API_KEY` in secrets
5. Deploy

**Your Navo app will be live and accessible to anyone.**

## Need Help?

- Check the full README.md
- Review the code in navo.py
- Open an issue on GitHub
