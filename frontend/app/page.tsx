"use client";

import HotelData from "@/components/HotelData";
import InputForm from "@/components/InputForm";
import Loading from "@/components/Loading";
import Navbar from "@/components/Navbar";
import { BlobState, HotelDataType } from "@/types";

import React, { useState, useRef  } from "react";

const Home = () => {
  const [hotelData, setHotelData] = useState<HotelDataType | null>(null);
  const downloadButtonRef = useRef<HTMLButtonElement | null>(null);


  const [loaderHotelData, setLoaderHotelData] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [blobData, setBlobData] = useState<BlobState>(null);

  const handleSetHotelData = (data: HotelDataType) => {
    setHotelData(data);
     // Scroll to the download button
     if (downloadButtonRef.current) {
      downloadButtonRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleLoader = (data: boolean) => {
    setLoaderHotelData(data);
  };

  const handleDownloadCSV = async (hotelName: string) => {
    console.log("blobData", blobData);
  
    if (blobData) {
      // Convert the CSV string to Blob
      const csvBlob = new Blob([blobData], { type: 'text/csv' });
  
      // Create an Object URL from the Blob
      const url = window.URL.createObjectURL(csvBlob);
  
      const a = document.createElement("a");
      a.style.display = "none";
      a.href = url;
      // the filename you want
      a.download = `${hotelName}_reviews.csv`;
  
      document.body.appendChild(a);
      a.click();
  
      window.URL.revokeObjectURL(url);
    }
  };
  
  return (
    <>
      <div className="flex-col items-center justify-center w-full">
        <Navbar />

        <InputForm
          handleSetHotelData={handleSetHotelData}
          handleLoader={handleLoader}
          hotelData={hotelData}
          setLoading={setLoading}
          loading={loading}
          setBlobData={setBlobData}
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
                  <div className="flex flex-col">
                    <HotelData hotelInfo={hotelData} />
                    {loading === false && (
                      <button
                        ref={downloadButtonRef}
                        type="button"
                        className="mt-6 text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-6"
                        onClick={() => handleDownloadCSV(hotelData.hotelName)}
                      >
                        Dowload Reviews
                      </button>
                    )}
                  </div>
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
