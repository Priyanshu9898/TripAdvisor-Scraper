import React from "react";
import ThemeButton from "./ThemeButton";


const Navbar = () => {
  return (
    <div className="flex w-full h-[64px] items-center justify-between p-4 bg-gray-900">
      <div className="text-xl md:text-2xl lg:text-3xl">Hotel Reviews Scraper</div>
      <div>
        {/* <ModeToggle /> */}
        <ThemeButton />
      </div>
    </div>
  );
};

export default Navbar;
