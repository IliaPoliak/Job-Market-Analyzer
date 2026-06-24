import { useState, useEffect, useRef, useMemo } from "react";

import { TOP_N, CATEGORY_COLORS } from "../utils/config";
import { shortenArray } from "../utils/utils";
import type { Skill, StateSetter } from "../utils/types";

import {
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  BarChart,
  Bar,
  ResponsiveContainer,
  Cell,
} from "recharts";

function SkillsPage({
  skills,
  expanded,
  setExpanded,
}: {
  skills: Skill[];
  expanded: boolean;
  setExpanded: StateSetter<boolean>;
}) {
  // Selected Categories Set to filter skills
  const [selectedCategories, setSelectedCategories] = useState<Set<string>>(
    new Set(),
  );

  // Skills Filtering UI
  const [filterOpen, setFilterOpen] = useState<boolean>(false);
  const filterRef = useRef<HTMLDivElement>(null);

  // Filter skills
  const filteredSkills = useMemo(() => {
    if (selectedCategories.size === 0) return skills;
    return skills.filter((s) => selectedCategories.has(s.category));
  }, [skills, selectedCategories]);

  // Create an event listener to close dropdown when clicking outside it
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (filterRef.current && !filterRef.current.contains(e.target as Node)) {
        setFilterOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // Declare function to toggle category
  const toggleCategory = (cat: string) => {
    setSelectedCategories((prev) => {
      const next = new Set(prev);
      next.has(cat) ? next.delete(cat) : next.add(cat);
      return next;
    });
  };

  // Shorten the data to first show the shorten graph and then expand when clicked
  const skillsShorten = useMemo(
    () =>
      shortenArray(filteredSkills, {
        skill: "Others",
        category: "Others",
        count: 0,
      }),
    [filteredSkills],
  );

  // Change the data displaed depending on the expanded state
  const skillsListToDisplay = useMemo(() => {
    if (expanded) {
      return filteredSkills;
    } else {
      return skillsShorten;
    }
  }, [expanded, filteredSkills]);

  return (
    <>
      {/* Filter Button */}
      <div className="relative mr-2 inline-block" ref={filterRef}>
        <button onClick={() => setFilterOpen((o) => !o)} className="button">
          Filter
          {selectedCategories.size > 0 && ` (${selectedCategories.size})`}
        </button>

        {/* Filter Dropdown */}
        {filterOpen && (
          <div className="absolute z-10 mt-2 w-60 rounded-md border border-gray-200 bg-white p-2 shadow-lg">
            <div className="flex items-center justify-between px-2 pb-2">
              <span className="text-xs font-medium text-gray-500">
                Categories
              </span>
              <button
                onClick={() => setSelectedCategories(new Set())}
                className="text-xs text-blue-600 hover:underline cursor-pointer"
              >
                Clear
              </button>
            </div>
            <div className="max-h-64 overflow-y-auto">
              {Object.keys(CATEGORY_COLORS).map((cat) => (
                <label
                  key={cat}
                  className="flex items-center gap-2 rounded px-2 py-1 text-sm hover:bg-gray-50 cursor-pointer"
                >
                  <input
                    type="checkbox"
                    checked={selectedCategories.has(cat)}
                    onChange={() => toggleCategory(cat)}
                    className="h-3.5 w-3.5 rounded border-gray-300"
                  />
                  <span
                    className="h-2 w-2 rounded-full"
                    style={{
                      backgroundColor:
                        CATEGORY_COLORS[cat as keyof typeof CATEGORY_COLORS] ||
                        "#95A5A6",
                    }}
                  />
                  {cat}
                </label>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Expand Button */}
      {skills.length > TOP_N && (
        <button onClick={() => setExpanded(!expanded)} className="button">
          {expanded ? "Collapse" : "Expand"}
        </button>
      )}

      {/* Graph */}
      <ResponsiveContainer
        width="90%"
        height={skillsListToDisplay.length * 30 + 70}
      >
        <BarChart
          data={skillsListToDisplay}
          layout="vertical"
          margin={{ top: 20, right: 30, left: 120, bottom: 20 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" />
          <YAxis dataKey="skill" type="category" width={200} />
          <Tooltip
            labelFormatter={(label) => {
              const category = skillsListToDisplay.find(
                (item) => item.skill === label,
              )?.category;

              const color =
                CATEGORY_COLORS[category as keyof typeof CATEGORY_COLORS] ||
                "#95A5A6";

              return (
                <span>
                  {label}
                  <span
                    style={{
                      color: color,
                      fontWeight: "bold",
                      marginLeft: "4px",
                    }}
                  >
                    ({category})
                  </span>
                </span>
              );
            }}
            formatter={(value) => [`${value}`, "Mentions"]}
          />
          <Bar dataKey="count">
            {skillsListToDisplay.map((entry, index) => (
              <Cell
                key={`cell-${index}`}
                fill={
                  CATEGORY_COLORS[
                    entry.category as keyof typeof CATEGORY_COLORS
                  ] || "#95A5A6"
                }
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </>
  );
}

export default SkillsPage;
