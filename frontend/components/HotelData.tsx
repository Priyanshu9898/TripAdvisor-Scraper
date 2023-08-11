import React, { FC } from "react";
import { Button, Card } from "flowbite-react";
import { HotelDataType } from "@/types";
import HotelInfoBox from "./HotelInfoBox";

const HotelData: FC<{ hotelInfo: HotelDataType }> = ({ hotelInfo }) => {
  return (
    <>
      <Card className="w-full md:w-[700px] lg:w-[70vw]">
        <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
          <p>Hotel Data</p>
        </h5>

        <div className="grid gap-4">
          <div>
            <HotelInfoBox
              keyValue={"Hotel Name:"}
              value={hotelInfo.hotelName}
            />

            <HotelInfoBox
              keyValue={"Hotel Address:"}
              value={hotelInfo.hotelAddress}
            />

            <HotelInfoBox
              keyValue={"Hotel Rating:"}
              value={hotelInfo.hotelRating}
            />

            <HotelInfoBox
              keyValue={"Total Reviews:"}
              value={hotelInfo.totalNumberOfReviews}
            />
          </div>
        </div>
      </Card>
    </>
  );
};

export default HotelData;
