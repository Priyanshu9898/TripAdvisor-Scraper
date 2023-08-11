import React from "react";
import ThemeButton from "./ThemeButton";


const Navbar = () => {
  return (
    <div className="flex w-full items-center justify-between p-4 bg-gray-900">
      <div className="">Hotel Reviews Scraper</div>
      <div>
        {/* <ModeToggle /> */}
        {/* <ThemeButton /> */}
      </div>
    </div>
  );
};

export default Navbar;
