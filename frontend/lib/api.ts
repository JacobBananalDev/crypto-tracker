/**
 * api.ts
 *
 * Centralized API client used by the frontend to communicate
 * with the FastAPI backend.
 *
 * Why do this?
 *
 * Instead of calling fetch() everywhere in components,
 * we place all API logic in one location.
 *
 * Benefits:
 * - cleaner components
 * - easier debugging
 * - easier API updates
 * - reusable requests
 */

const API_BASE = "http://localhost:8000/api/v1"

/**
 * Fetch total portfolio value and asset breakdown.
 *
 * Endpoint:
 * GET /api/v1/portfolio/value
 */
export async function getPortfolioValue() {
  const res = await fetch(`${API_BASE}/portfolio/value`)

  if (!res.ok) {
    throw new Error("Failed to fetch portfolio value")
  }

  return res.json()
}

/**
 * Fetch all tracked coins.
 *
 * Endpoint:
 * GET /api/v1/coins
 */
export async function getCoins() {
  const res = await fetch(`${API_BASE}/coins`)

  if (!res.ok) {
    throw new Error("Failed to fetch coins")
  }

  return res.json()
}

/**
 * Fetch chart-ready price data for a given coin symbol.
 *
 * Endpoint:
 * GET /api/v1/coins/{symbol}/chart
 *
 * Example:
 * getCoinChart("BTC")
 */
export async function getCoinChart(symbol: string) {
  const res = await fetch(`${API_BASE}/coins/${symbol}/chart`)

  if (!res.ok) {
    throw new Error(`Failed to fetch chart data for ${symbol}`)
  }

  return res.json()
}