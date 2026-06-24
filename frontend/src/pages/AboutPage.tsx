function AboutPage() {
  return (
    <p className="text-lg font-medium text-gray-800">
      On this web page, you can view an analysis of the current job market state
      by clicking through the different tabs. The job postings that the
      information is taken from are specifically IT positions in Bratislava. To
      get more information, please visit the project page on{" "}
      <a
        href="https://github.com/IliaPoliak/Job-Market-Analyzer"
        className="text-blue-600 hover:underline cursor-pointer"
      >
        GitHub
      </a>
      .
    </p>
  );
}

export default AboutPage;
