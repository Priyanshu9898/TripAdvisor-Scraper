import axios from "axios";
import { Button } from "flowbite-react";
import { BACKEND_URL } from "@/Utils/APIEndpoint";
import { FC, useEffect, useState } from "react";
import { BlobState, HotelDataType } from "@/types";

const InputForm: FC<{
  handleSetHotelData: (arg: HotelDataType) => void;
  handleLoader: (arg: boolean) => void;
  hotelData: HotelDataType | null;
  setLoading: (arg: boolean) => void;
  loading: boolean;
  setBlobData: (arg: any) => void;
}> = ({ handleSetHotelData, handleLoader, hotelData, setLoading, loading , setBlobData}) => {
  // const [loading, setLoading] = useState<boolean>(false);
  const [errors, setErrors] = useState({ url: "", numReviews: "" });
  // const [blobData, setBlobData] = useState<BlobState>(null);
  const [data, setData] = useState({
    url: "",
    numReviews: 0,
  });

  const fetchReviews = async () => {
    try {

      const config = {
        headers: {
          'Content-type': 'application/json',
        },

        withCredentials: true,
      }

      const response: any = await axios.post(`${BACKEND_URL}/generate-csv`, {
        url: data.url,
        numReviews: data.numReviews,
      },config);
      console.log(response);
      // const blob = await response.blob();
      setBlobData(response.data);
      setLoading(false);
    } catch (err) {
      console.log(err);
      setLoading(false);
    }
  };

  // useEffect(() => {
  //   fetchReviews();
  // }, [hotelData]);

  const handleChange = (e: any) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };

  const validateForm = () => {
    let formErrors = { url: "", numReviews: "" };

    if (!data.url.startsWith("https://www.tripadvisor.com")) {
      formErrors.url = "Invalid TripAdvisor URL.";
    }

    if (data.numReviews <= 0) {
      formErrors.numReviews = "Please enter a valid number of reviews.";
    }

    setErrors(formErrors);
    return !Object.values(formErrors).some((error) => error !== "");
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    if (!validateForm()) return;

    const url = data.url;

    try {
      setLoading(true);
      handleLoader(true);
      const config = {
        headers: {
          'Content-type': 'application/json',
        },

        withCredentials: true,
      }
      const response = await axios.post(`${BACKEND_URL}/getHotelData`, {
        url: url,
      }, config);
      console.log(response.data);

      handleSetHotelData(response.data);
      handleLoader(false);
    } catch (err) {
      console.log(err);
      handleLoader(false);
      setLoading(false);
    }

    fetchReviews();
  };

  

  return (
    <div className="w-full flex items-center justify-center mt-14">
      <form
        className="w-full p-2 md:p-0 md:w-[700px] lg:w-[65vw] flex-col items-center justify-center"
        onSubmit={handleSubmit}
      >
        <div className="mb-6">
          <label
            htmlFor="url"
            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >
            Hotel URL
          </label>
          <input
            type="url"
            id="url"
            name="url"
            value={data.url}
            onChange={handleChange}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Enter TripAdvisor Hotel URL"
            required
          />
          <span className="text-red-600 text-sm">{errors.url}</span>
        </div>
        <div className="mb-6">
          <label
            htmlFor="totalReviews"
            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >
            Number of Reviews
          </label>
          <input
            type="number"
            id="numReviews"
            name="numReviews"
            value={data.numReviews}
            onChange={handleChange}
            placeholder="0"
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required
          />
          <span className="text-red-600 text-sm">{errors.numReviews}</span>
        </div>

        <Button
          gradientDuoTone="purpleToBlue"
          type="submit"
          isProcessing={loading}
        >
          Submit
        </Button>
      </form>
    </div>
  );
};

export default InputForm;
