import { useMemo } from "react";

import { TOP_N } from "../utils/config";
import { shortenArray } from "../utils/utils";
import type { Company, StateSetter } from "../utils/types";

import {
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  BarChart,
  Bar,
  ResponsiveContainer,
} from "recharts";

function CompaniesPage({
  companies,
  expanded,
  setExpanded,
}: {
  companies: Company[];
  expanded: boolean;
  setExpanded: StateSetter<boolean>;
}) {
  // Shorten the data to first show the shorten graph and then expand when clicked
  const companiesShorten = useMemo(
    () =>
      shortenArray(companies, {
        company: "Others",
        count: 0,
      }),
    [companies],
  );

  // Change the data displaed depending on the expanded state
  const companiesListToDisplay = useMemo(() => {
    if (expanded) {
      return companies;
    } else {
      return companiesShorten;
    }
  }, [expanded, companies]);

  return (
    <>
      {/* Expand Button */}
      {companies.length > TOP_N && (
        <button onClick={() => setExpanded(!expanded)} className="button">
          {expanded ? "Collapse" : "Expand"}
        </button>
      )}

      {/* Graph */}
      <ResponsiveContainer
        width="90%"
        height={companiesListToDisplay.length * 30 + 70}
      >
        <BarChart
          data={companiesListToDisplay}
          layout="vertical"
          margin={{ top: 20, right: 30, left: 20, bottom: 20 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" />
          <YAxis dataKey="company" type="category" width={300} />
          <Tooltip formatter={(value) => [`${value}`, "Job Postings"]} />
          <Bar dataKey="count" fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>
    </>
  );
}

export default CompaniesPage;
