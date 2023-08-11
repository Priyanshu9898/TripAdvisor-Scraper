"use client";

import HotelData from "@/components/HotelData";
import InputForm from "@/components/InputForm";
import Navbar from "@/components/Navbar";
import { HotelDataType } from "@/types";
import React, { useState } from "react";

const Home = () => {
  const [hotelData, setHotelData] = useState<HotelDataType | null>(null);

  const handleSetHotelData = (data: HotelDataType) => {
    setHotelData(data);
  };

  return (
    <>
      <div className="flex-col items-center justify-center w-full">
        <Navbar />

        <InputForm handleSetHotelData={handleSetHotelData} />

        <div className="w-full flex items-center justify-center mt-12">
          {hotelData && (
            <>
              <HotelData hotelInfo={hotelData} />
            </>
          )}
        </div>
      </div>
    </>
  );
};

export default Home;
