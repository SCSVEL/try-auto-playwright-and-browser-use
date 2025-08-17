declare module "auto-playwright" {
  import { Page } from "@playwright/test";
  import { TestType } from "@playwright/test";
  export type Test = TestType<any, any>;
  export function auto(
    task: string,
    config: { page: Page; test?: Test },
    options?: any
  ): Promise<any>;
}
