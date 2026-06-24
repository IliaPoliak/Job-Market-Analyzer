export type StateSetter<T> = React.Dispatch<React.SetStateAction<T>>;

export interface Skill {
  skill: string;
  category: string;
  count: number;
}

export interface Company {
  company: string;
  count: number;
}
