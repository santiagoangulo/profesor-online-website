import fs from "fs";
import path from "path";

function deleteNjk(dir) {
  if (!fs.existsSync(dir)) return;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      deleteNjk(full);
    } else if (entry.name.endsWith(".njk")) {
      fs.unlinkSync(full);
    }
  }
}

export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("app.js");
  eleventyConfig.addPassthroughCopy("base.css");
  eleventyConfig.addPassthroughCopy("style.css");
  eleventyConfig.addPassthroughCopy("inner-pages.css");
  eleventyConfig.addPassthroughCopy("home.css");
  eleventyConfig.addPassthroughCopy("robots.txt");
  eleventyConfig.addPassthroughCopy("sitemap.xml");
  eleventyConfig.addPassthroughCopy("google*.html");

  eleventyConfig.addFilter("date", function (dateObj) {
    try {
      return new Date(dateObj).toLocaleDateString("es-ES", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    } catch {
      return dateObj;
    }
  });

  eleventyConfig.ignores.add("material_didactico/**");
  eleventyConfig.ignores.add("convert_exercises.py");
  eleventyConfig.ignores.add("node_modules/**");
  eleventyConfig.ignores.add("_site/**");
  eleventyConfig.addPassthroughCopy("material-didactico/es/**/index.html");
  eleventyConfig.addPassthroughCopy("material-didactico/en/**/index.html");

  eleventyConfig.on("afterBuild", () => {
    deleteNjk("_site");
  });

  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
    },
    templateFormats: ["njk", "md", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    htmlOutputSuffix: "",
  };
}
