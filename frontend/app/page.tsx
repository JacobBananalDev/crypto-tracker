/**
 * page.tsx
 *
 * Main dashboard page for the crypto tracker frontend.
 *
 * This page fetches portfolio value data from the FastAPI backend
 * and displays the user's total portfolio value along with each
 * asset's contribution.
 */

"use client";

import { useEffect, useState } from "react";
import { getPortfolioValue, getCoinChart } from "@/lib/api";
import PriceChart from "@/components/charts/PriceChart";

interface Asset {
  symbol: string;
  amount: number;
  price_usd: number;
  value_usd: number;
}

interface PortfolioResponse {
  total_value_usd: number;
  assets: Asset[];
}

export default function HomePage() {
  const [portfolio, setPortfolio] = useState<PortfolioResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [btcChart, setBtcChart] = useState<{ time: string; price: number }[]>(
    []
  );
  const [selectedCoin, setSelectedCoin] = useState("BTC");

  /**
   * Fetch portfolio value when the page loads.
   */
  useEffect(() => {
    async function fetchPortfolio() {
      try {
        const data = await getPortfolioValue();
        setPortfolio(data);
      } catch (error) {
        console.error("Failed to load portfolio", error);
      } finally {
        setLoading(false);
      }
    }

    fetchPortfolio();
  }, []);

  /**
   * Fetch chart data whenever the selected coin changes
   */

  useEffect(() => {
    async function fetchChart() {
      try {
        const chart = await getCoinChart(selectedCoin);

        setBtcChart(chart);
      } catch (error) {
        console.error("Failed to load chart", error);
      }
    }

    fetchChart();
  }, [selectedCoin]);

  if (loading) {
    return <div className="p-10 text-lg">Loading portfolio...</div>;
  }

  return (
    <main className="p-10 space-y-8">
      <h1 className="text-3xl font-bold mb-6">Crypto Portfolio Dashboard</h1>

      {/* Portfolio Value Card */}
      {portfolio && (
        <div className="bg-gray-900 text-white p-6 rounded-xl shadow-lg">
          <h2 className="text-xl mb-2">Total Portfolio Value</h2>

          <p className="text-4xl font-bold mb-6">
            ${portfolio.total_value_usd.toFixed(2)}
          </p>

          <div className="space-y-2">
            {portfolio.assets.map((asset) => (
              <div
                key={asset.symbol}
                className="flex justify-between border-b border-gray-700 pb-2"
              >
                <span>{asset.symbol}</span>

                <span>{asset.amount}</span>

                <span>${asset.value_usd.toFixed(2)}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="flex gap-4 mb-4">
        {["BTC", "SOL", "XRP"].map((coin) => (
          <button
            key={coin}
            onClick={() => setSelectedCoin(coin)}
            className={`px-4 py-2 rounded-lg ${
              selectedCoin === coin
                ? "bg-blue-500 text-white"
                : "bg-gray-800 text-gray-300"
            }`}
          >
            {coin}
          </button>
        ))}
      </div>

      {/* BTC Price Chart */}
      {btcChart.length > 0 && (
        <PriceChart title={`${selectedCoin} Price History`} data={btcChart} />
      )}
    </main>
  );
}
