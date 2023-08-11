"use client";

import HotelData from "@/components/HotelData";
import InputForm from "@/components/InputForm";
import Loading from "@/components/Loading";
import Navbar from "@/components/Navbar";
import { HotelDataType } from "@/types";
import React, { useState } from "react";

const Home = () => {
  const [hotelData, setHotelData] = useState<HotelDataType | null>(null);

  const [loaderHotelData, setLoaderHotelData] = useState<boolean>(false);

  const handleSetHotelData = (data: HotelDataType) => {
    setHotelData(data);
  };

  const handleLoader= (data: boolean) => {
    setLoaderHotelData(data);
  }

  return (
    <>
      <div className="flex-col items-center justify-center w-full">
        <Navbar />

        <InputForm
          handleSetHotelData={handleSetHotelData}
          handleLoader={handleLoader}
        />

        <div className="w-full flex items-center justify-center mt-12">
          {loaderHotelData === true ? (
            <>
              <Loading />
            </>
          ) : (
            <>
              {hotelData && (
                <>
                  <HotelData hotelInfo={hotelData} />
                </>
              )}
            </>
          )}
        </div>
      </div>
    </>
  );
};

export default Home;
