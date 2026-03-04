/**
 * PriceChart.tsx
 *
 * Reusable chart component for displaying crypto price history.
 *
 * We keep charts in a shared component so multiple pages
 * (dashboard, coin detail pages, etc.) can reuse the same chart UI.
 */

"use client"

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts"

type PricePoint = {
  time: string
  price: number
}

type Props = {
  title: string
  data: PricePoint[]
}

export default function PriceChart({ title, data }: Props) {
  return (
    <div className="bg-gray-900 text-white p-6 rounded-xl shadow-lg">
      <h3 className="text-lg font-semibold mb-4">{title}</h3>

      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={[...data].reverse()}>
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="price" dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}