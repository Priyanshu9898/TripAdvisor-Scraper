import React, { FC } from "react";


const HotelInfoBox: FC<{ keyValue: string; value: string | number }> = ({
  keyValue,
  value,
}) => {
  return (
    <>
      <div className="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0 mt-2">
        <span className="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500" />
        <div className="space-y-1">
          <p className="text-lg font-medium leading-none">{keyValue}</p>
          <p className="text-md text-muted-foreground flex-wrap text-gray-500 dark:text-gray-400">{value}</p>
          <hr />
        </div>
      </div>
    </>
  );
};

export default HotelInfoBox;
