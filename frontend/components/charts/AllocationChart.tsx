/**
 * AllocationChart.tsx
 *
 * Displays a pie chart showing how much of the portfolio
 * each asset represents.
 *
 * This helps users visually understand their asset allocation.
 */

"use client"

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts"

type Asset = {
  symbol: string
  value_usd: number
}

type Props = {
  assets: Asset[]
}

const COLORS = [
  "#3b82f6",
  "#22c55e",
  "#f59e0b",
  "#ef4444",
  "#8b5cf6"
]

export default function AllocationChart({ assets }: Props) {

  return (
    <div className="bg-gray-900 text-white p-6 rounded-xl shadow-lg">

      <h3 className="text-lg font-semibold mb-4">
        Portfolio Allocation
      </h3>

      <div className="h-72">

        <ResponsiveContainer width="100%" height="100%">

          <PieChart>

            <Pie
              data={assets}
              dataKey="value_usd"
              nameKey="symbol"
              outerRadius={120}
              label
            >

              {assets.map((entry, index) => (

                <Cell
                  key={entry.symbol}
                  fill={COLORS[index % COLORS.length]}
                />

              ))}

            </Pie>

            <Tooltip />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  )

}