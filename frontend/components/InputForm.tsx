"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import * as z from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Label } from "./ui/label";

const FormSchema = z.object({
  url: z.string().url().min(2),
  numReviews: z.number().gt(0),
});

const InputForm = () => {
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
  });

  function onSubmit(data: z.infer<typeof FormSchema>) {
    console.log(data);
  }

  return (
    <div className="w-full h-screen flex items-start justify-center mt-14">
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="w-2/3 space-y-6"
        >
          <FormField
            control={form.control}
            name="url"
            render={({ field }) => (
              <FormItem>
                <Label>Hotel URL</Label>
                <FormControl>
                  <Input placeholder="Enter Your URL..." {...field} />
                </FormControl>
                <FormDescription>
                  Enter Your TripAdvisor Hotel URL
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="numReviews"
            render={({ field }) => (
              <FormItem>
                <Label>Number of Reviews</Label>
                <FormControl>
                  <Input
                    type="number"
                    min={0}
                    {...field}
                    placeholder="0"
                    onChange={(event) => field.onChange(+event.target.value)}
                  />
                </FormControl>
                <FormDescription>
                  Enter Number of Reviews you want to collect
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit" className="">
            Submit
          </Button>
        </form>
      </Form>
    </div>
  );
};

export default InputForm;
