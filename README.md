# Sentiment Analysis API

A simple REST API that analyzes the sentiment of text input and returns the sentiment polarity and classification (positive, neutral, negative).

---

## Base URL

https://sentiment-analysis-api-cho0.onrender.com

---

## Endpoints

### GET /

Returns a welcome message.

**Response example:**

```json
{
  "message": "Welcome to the Sentiment Analysis API!"
}
```
 


### POST /analyze
Accepts JSON with a text field and returns the sentiment analysis.

**Request body example:**
```json
{
  "text": "I love building APIs!"
}
```

**Response example:**
```json
{
  "text": "I love building APIs!",
  "polarity": 0.625,
  "sentiment": "positive"
}
```
## Usage
No authentication required.
