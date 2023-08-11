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
import { Separator } from "@/components/ui/separator";
import { HotelDataType } from "@/types";


const HotelData: FC<{hotelInfo: HotelDataType}> = ({hotelInfo}) => {
  return (
    <>
      <Card className="w-full md:w-[700px] lg:w-[900px]">
        <CardHeader>
          <CardTitle>Results</CardTitle>
          {/* <CardDescription>You have 3 unread messages.</CardDescription> */}
        </CardHeader>
        <CardContent className="grid gap-4">
          <div>
            <div className="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0">
              <span className="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500" />
              <div className="space-y-1">
                <p className="text-sm font-medium leading-none"></p>
                <p className="text-sm text-muted-foreground"></p>
              </div>
            </div>
          </div>
        </CardContent>
     
      </Card>
    </>
  );
};

export default HotelData;
