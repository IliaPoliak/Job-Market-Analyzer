import { TOP_N } from "./config.ts";
import type { StateSetter } from "./types.ts";

type DataSetter<T> = StateSetter<T>;
type LoadingSetter = StateSetter<boolean>;
type ErrorSetter = StateSetter<string | null>;

export async function fetchData<T>(
  endpoint: string,
  setData: DataSetter<T>,
  setLoading: LoadingSetter,
  setError: ErrorSetter,
) {
  setLoading(true);
  setError(null);
  try {
    const response = await fetch(endpoint);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    setData(data);
  } catch (err) {
    setError(err instanceof Error ? err.message : "An error occurred");
  } finally {
    setLoading(false);
  }
}

export function shortenArray<T extends { count: number }>(
  array: T[],
  other: T,
): T[] {
  // Early return if array is empty
  if (!array || array.length === 0) {
    return [];
  }

  let arrayTop: T[] = [];

  for (let i = 0; i < array.length; i++) {
    if (i < TOP_N) {
      arrayTop.push(array[i]);
    } else {
      other.count += array[i].count;
    }
  }
  if (other.count > 0) arrayTop.push(other);

  return arrayTop;
}
