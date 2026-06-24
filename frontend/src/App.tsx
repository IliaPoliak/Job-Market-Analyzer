import { useState, useEffect } from "react";

import { API_BASE } from "./utils/config";
import type { Skill, Company } from "./utils/types";
import { fetchData } from "./utils/utils";

import AboutPage from "./pages/AboutPage";
import SkillsPage from "./pages/SkillsPage";
import CompaniesPage from "./pages/CompaniesPage";

function App() {
  // The Page to display
  type Page = "About" | "Skills" | "Companies";
  const pages: Page[] = ["About", "Skills", "Companies"]; // Array of all available pages to display tabs
  const [currentPage, setCurrentPage] = useState<Page>("About");

  // Declare the graph data to be filled via api call later
  const [skills, setSkills] = useState<Skill[]>([]);
  const [companies, setCompanies] = useState<Company[]>([]);

  // Loading and Error states for an api call
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch relevant data when clicking to the page
  useEffect(() => {
    if (currentPage === "Skills") {
      fetchData(`${API_BASE}/relevant_skills`, setSkills, setLoading, setError);
    } else if (currentPage === "Companies") {
      fetchData(
        `${API_BASE}/most_hiring_companies`,
        setCompanies,
        setLoading,
        setError,
      );
    }
  }, [currentPage]);

  // Whether to show the full graph or not
  const [expanded, setExpanded] = useState<boolean>(false);

  // Reset expanded state and selected categories when changing the page
  useEffect(() => {
    setExpanded(false);
  }, [currentPage]);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="mx-auto max-w-5xl">
        {/* HEADING */}
        <h1 className="heading">Job Market Analyzer</h1>

        {/* TABS */}
        <div className="flex gap-1">
          {pages.map((page) => (
            <button
              key={page}
              onClick={() => setCurrentPage(page)}
              className={`tab-base ${
                currentPage === page ? "highlighted-tab" : "not-highlighted-tab"
              }`}
            >
              {page}
            </button>
          ))}
        </div>

        {/* PANEL */}
        <div className="rounded-b-lg rounded-tr-lg border border-gray-200 bg-white p-6 shadow-sm">
          {/* About */}
          {currentPage === "About" && <AboutPage />}

          {/* Skills */}
          {currentPage === "Skills" && (
            <SkillsPage
              skills={skills}
              expanded={expanded}
              setExpanded={setExpanded}
            />
          )}

          {/* Companies */}
          {currentPage === "Companies" && (
            <CompaniesPage
              companies={companies}
              expanded={expanded}
              setExpanded={setExpanded}
            />
          )}

          {/* Loading */}
          {loading && currentPage !== "About" && (
            <p className="loading">Loading...</p>
          )}

          {/* Error */}
          {error && currentPage !== "About" && (
            <p className="error">Error: {error}</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
