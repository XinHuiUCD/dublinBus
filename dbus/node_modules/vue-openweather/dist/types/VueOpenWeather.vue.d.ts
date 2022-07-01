declare const _default: import("vue").DefineComponent<{
    apiKey: StringConstructor;
    lat: StringConstructor;
    long: StringConstructor;
    hourly: {
        type: BooleanConstructor;
        default: boolean;
    };
    daily: {
        type: BooleanConstructor;
        default: boolean;
    };
    units: {
        type: StringConstructor;
        default: string;
    };
    excludes: {
        type: ArrayConstructor;
        default: string[];
    };
}, () => void, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, "weatherData"[], "weatherData", import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    apiKey: StringConstructor;
    lat: StringConstructor;
    long: StringConstructor;
    hourly: {
        type: BooleanConstructor;
        default: boolean;
    };
    daily: {
        type: BooleanConstructor;
        default: boolean;
    };
    units: {
        type: StringConstructor;
        default: string;
    };
    excludes: {
        type: ArrayConstructor;
        default: string[];
    };
}>> & {
    onWeatherData?: ((...args: any[]) => any) | undefined;
}, {
    hourly: boolean;
    daily: boolean;
    units: string;
    excludes: unknown[];
}>;
export default _default;
