# LG Customer Segmentation & Pricing API

This Flask API provides endpoints for:

- Predicting customer clusters
- Viewing cluster profiles
- Viewing cluster insights
- Price elasticity summaries
- Price simulation for clusters

## Deployment

This app is ready to deploy on [Render](https://render.com) using `render.yaml`.

## Endpoints

- `GET /` → Health check
- `POST /predict` → JSON: `{"features": [Age, Income, LoyaltyScore, OnlineEngagement]}`
- `GET /cluster_profile/<cluster_id>`
- `GET /cluster_insights`
- `GET /elasticity`
- `POST /simulate_price` → JSON: `{"cluster_id": int, "price": float}`

## Usage Example

```bash
curl -X POST https://your-app.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"features": [34, 45000, 70, 0.85]}'
