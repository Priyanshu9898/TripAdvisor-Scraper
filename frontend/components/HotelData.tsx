import React, { FC } from "react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { HotelDataType } from "@/types";
import HotelInfoBox from "./HotelInfoBox";

const HotelData: FC<{ hotelInfo: HotelDataType }> = ({ hotelInfo }) => {
  return (
    <>
      <Card className="w-full md:w-[700px] lg:w-[900px]">
        <CardHeader>
          <CardTitle>Hotel Data</CardTitle>
        </CardHeader>
        <CardContent className="grid gap-4">
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
        </CardContent>
      </Card>
    </>
  );
};

export default HotelData;
